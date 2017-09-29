#!/bin/sh

init_env(){
    /etc/init.d/openvpn stop
    cd /usr/share/easy-rsa/2.0 && source ./vars
}

#judge is not root exit programe! and stop openvpn and init opvpn cert
[ ! $USER = "root" ] && echo "oh,pls use root execute $0" && exit 1

#read opvpn username and general password
read -t 20 -p 'pls input the username:' user || exit 1
secret=`openssl rand -hex 8`
unzip_pass=`openssl rand -hex 16`
init_cert_bak_dir(){
    #create ovpn cert_bak_dir if not exist
    [ -e /server/openvpn_accout_bak ] || mkdir /server/openvpn_accout_bak
    [ ! -e /server/openvpn_accout_bak/tt100.ovpn ] && exit 1
    [ -e /server/openvpn_accout_bak/$user ] && exit 1 || \
    mkdir /server/openvpn_accout_bak/$user
}

create_passfile(){
    #write cert password to user_ovpn_dir
    echo "cert_password: $secret" > /server/openvpn_accout_bak/${user}/${user}_pass_$(date +%F).txt
    #general cert
    #[ -e /server/shells/gg_vpn_keys.exp ] && \
    #expect /server/shells/gg_vpn_keys.exp $user $secret
    #sleep 5


    #generay cert manually
    echo
    echo "cert secret is: $secret"
    echo
    #cd /usr/share/easy-rsa/2.0 && ./build-key-pass $user
    cd /usr/share/easy-rsa/2.0 && ./build-key $user
    sleep 2
    #copy cert to user_ovpn_dir
    cp /usr/share/easy-rsa/2.0/keys/ca.crt /server/openvpn_accout_bak/$user
    cp /usr/share/easy-rsa/2.0/keys/ta.key /server/openvpn_accout_bak/$user
    cp /usr/share/easy-rsa/2.0/keys/${user}* /server/openvpn_accout_bak/$user
    rm -f /server/openvpn_accout_bak/${user}/${user}.csr
    #generay gg code
    useradd $user && chown -R ${user}.$user /server/openvpn_accout_bak/$user

    gg=`sudo su - $user -c /usr/local/bin/gg-auth.py`
    echo "google_code_url: $gg" >> /server/openvpn_accout_bak/${user}/${user}_pass_$(date +%F).txt
    #general gg qrcode
    cd /server/openvpn_accout_bak/${user} && qrencode -o ${user}_google_qrcode.png -t png -s 20 $gg
    #general client ovpn file
    cd /server/openvpn_accout_bak/ && cp tt100.ovpn $user/${user}.ovpn
    sed -i "s#tt100#${user}#g" $user/${user}.ovpn
    #general user.tar.gz file
    
    cd /server/openvpn_accout_bak/ && \
    zip -rP $unzip_pass ${user}_openvpn.zip ./$user
    echo
    echo
    echo "unzip_pass: $unzip_pass"
    echo
    echo "pls download cert pkgs: sz /server/openvpn_accout_bak/${user}_openvpn.zip"
    echo "good lucky"
}

main(){
    init_env
    init_cert_bak_dir
    create_passfile
}

main
/etc/init.d/openvpn start
netstat -ntulp|grep openvpn

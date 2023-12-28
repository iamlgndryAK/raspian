#update everything
function update(){ # update and reboot/shutdown
        # apt
        sudo apt update -y
        sudo apt upgrade -y
        sudo apt dist-upgrade -y
        sudo apt autoremove -y
        sudo apt autoclean -y

        # apt-get
        sudo apt-get update -y
        sudo apt-get upgrade -y
        sudo apt-get dist-upgrade -y
        sudo apt-get dselect-upgrade -y
        sudo apt-get autoremove -y
        
        # fwupdmgr
        sudo fwupdmgr get-devices
        sudo fwupdmgr get-updates
        sudo fwupdmgr update
        
        ##update BetterDiscord
        sudo betterdiscordctl self-upgrade

        # snap
        sudo snap refresh

        # homebrew
        brew upgrade
        
        # reboot/shutdown
        sudo $1 now
}

# linux-scripts
Various linux scripts that are needed on separate occasions

## Checklist

- [ ] Download neovim and use my nvim config (might need to remove the lazy folder if it shows up in an error)
- [ ] Install Thunderbird and import profile, CalDav,CardDav(use this [tutorial](https://portal.thobson.com/knowledgebase/213/How-to-sync-contacts-to-Mozilla-Thunderbird-via-CardDav.html))
- [ ] Install Zotero and import library from nextcloud webdav
- [ ] Install Zen browser, sync passwords, add essential tabs, tabs on right, tab unloader off, open previous tabs uncheck
- [ ] Install Nextcloud-Desktop and sync folders locally (will start to compile it from source)
- [ ] Install Openboard with a symbolic link to the nextcloud folder for syncing things
- [ ] Install KDE-Connect and sync commands and pair phone
- [ ] Install jetbrains-toolbox to download jetbrains IDEs(Android Studio mainly, Pycharm)
- [ ] Add .desktop files for running custom containers for frequently used services([ConvertX](https://github.com/C4illin/ConvertX/),[Stirling-Pdf](https://github.com/Stirling-Tools/Stirling-PDF))
- [ ] Download texlive for latex (or setup overleaf locally)
- [ ] Remove gnome games 
- [ ] Install Spotify
- [ ] Change a few gnome shortcuts
- [ ] Install Okular
- [ ] Add Music folder to Amberol
- [ ] Install Qt libraries(qt6-base-devel and qt6-base-common-devel should be enough as starters)
- [ ] Change fonts in the terminal (for neovim devicons to load properly, [Hack Nerd Font here](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Hack.zip))
- [ ] Pinning things to dock (browser,thunderbird,zotero,spotify,files,terminal)
- [ ] Install docker and docker-compose for containers

## Commands

`flatpak install flathub org.kde.Okular`

`flatpak install flathub org.zotero.Zotero`

`flatpak install flathub org.mozilla.Thunderbird`

`flatpak install flathub app.zen_browser.zen`

`flatpak install flathub com.nextcloud.desktopclient.nextcloud`

`flatpak install flathub com.spotify.Client`

`sudo zypper in qt6-base-devel qt6-base-common-devel`

`sudo zypper rm patterns-gnome-gnome_games`

`sudo zypper in OpenBoard`

`sudo zypper in docker docker-compose`

``
### Symlinks for nextcloud

#### Nautilus scripts
`ln -s ~/Nextcloud/Configuration/nautilus-scripts/* ~/.local/share/nautilus/scripts/`

`chmod +x ~/.local/share/nautilus/scripts/*`

#### Openboard documents

`rm -rf ~/.local/share/OpenBoard/document`

`ln -s ~/Nextcloud/openboard/ ~/.local/share/OpenBoard/document`

#### Music

(might need to recreate an OpenBoard folder)
`rm -rf ~/Music`

`ln -s ~/Nextcloud/Music ~/Music`

(The Music app in gnome does not support symlinked songs)
`flatpak install flathub io.bassi.Amberol`


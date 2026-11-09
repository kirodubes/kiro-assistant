# How-to Recipes

Step-by-step answers to common tasks. Each recipe gives the **ArchLinux Tweak
Tool route first**, then the terminal route. ATT runs in the user's language, so
each recipe lists the button labels in all 13 ATT translations: match the user's
language and quote the label they will actually see. Never translate a label
yourself — if a label is not listed here, describe its position instead.

Language codes: de German, es Spanish, fr French, hu Hungarian, it Italian, ja
Japanese, nl Dutch, pl Polish, pt_BR Brazilian Portuguese, ro Romanian, ru
Russian, tr Turkish, zh_CN simplified Chinese.

Launch ATT from the menu ("Arch Linux Tweak Tool") or with `att`. Never as
root: it asks for the password itself. The sidebar has a search box to find a
page by name.

## Switch the system language back to English

For a user stuck in a desktop language they can't read.

ATT:
1. Optional: the language dropdown at the top right of ATT → English → **Restart
   ATT**. This changes only ATT's own language.
2. Sidebar **Locale** → the page shows **Current Settings**.
3. Section **System Locale**: pick `en_US.UTF-8` → **Apply**. Apply also rewrites
   a leftover `LANGUAGE=` line in another language, which would otherwise keep
   the desktop in the old language.
4. Section **Individual Categories** → **Reset all to LANG**, to drop leftover
   number/currency/date overrides.
5. Log out and back in.

Terminal:
```
sudo localectl set-locale LANG=en_US.UTF-8
cat /etc/locale.conf
```
Remove any leftover `LANGUAGE=` or `LC_*` lines with `sudoedit /etc/locale.conf`,
then log out and in.

Button labels in every ATT language (from ATT's own translations):

- **Restart ATT** — de ATT neu starten · es Reiniciar ATT · fr Redémarrer ATT · hu ATT újraindítása · it Riavvia ATT · ja ATT を再起動 · nl ATT herstarten · pl Uruchom ponownie ATT · pt_BR Reiniciar o ATT · ro Repornește ATT · ru Перезапустить ATT · tr ATT'yi yeniden başlat · zh_CN 重启 ATT
- **Locale** — de Locale · es Idioma y región · fr Paramètres régionaux · hu Nyelvi beállítások · it Lingua e area geografica · ja ロケール · nl Taal en regio · pl Ustawienia regionalne · pt_BR Idioma · ro Setări regionale · ru Локаль · tr Yerel ayar · zh_CN 区域设置
- **Current Settings** — de Aktuelle Einstellungen · es Ajustes actuales · fr Paramètres actuels · hu Jelenlegi beállítások · it Impostazioni attuali · ja 現在の設定 · nl Huidige instellingen · pl Bieżące ustawienia · pt_BR Configurações atuais · ro Setări curente · ru Текущие настройки · tr Geçerli Ayarlar · zh_CN 当前设置
- **System Locale** — de System-Locale · es Configuración regional del sistema · fr Paramètres régionaux du système · hu Rendszer nyelve · it Lingua di sistema · ja システムロケール · nl Systeemtaal · pl Ustawienia regionalne systemu · pt_BR Locale do sistema · ro Localizarea sistemului · ru Системная локаль · tr Sistem Yerel Ayarı · zh_CN 系统区域设置
- **Apply** — de Anwenden · es Aplicar · fr Appliquer · hu Alkalmaz · it Applica · ja 適用 · nl Toepassen · pl Zastosuj · pt_BR Aplicar · ro Aplică · ru Применить · tr Uygulayın · zh_CN 应用
- **Individual Categories** — de Einzelne Kategorien · es Categorías individuales · fr Catégories individuelles · hu Egyes kategóriák · it Categorie singole · ja 個別のカテゴリ · nl Afzonderlijke categorieën · pl Poszczególne kategorie · pt_BR Categorias individuais · ro Categorii individuale · ru Отдельные категории · tr Tek Tek Kategoriler · zh_CN 单独类别
- **Reset all to LANG** — de Alle auf LANG zurücksetzen · es Restablecer todas a LANG · fr Tout réinitialiser sur LANG · hu Mind visszaállítása a LANG értékére · it Reimposta tutto su LANG · ja すべて LANG に戻す · nl Alles terugzetten naar LANG · pl Zresetuj wszystko do LANG · pt_BR Redefinir tudo para LANG · ro Resetează totul la LANG · ru Сбросить всё до значений LANG · tr Tümünü LANG'a sıfırla · zh_CN 全部重置为 LANG


## Change the keyboard layout

ATT: **Locale** → **Keyboard** tab → section "X11 / Wayland Keyboard": layout,
variant and an optional second layout (switch between the two with
`Alt` + `Shift`). "Console Keyboard (TTY)" → "Sync from X11" copies it to the
text console.

Terminal: `localectl set-x11-keymap be` (replace `be` with the layout code).

Button labels in every ATT language (from ATT's own translations):

- **Locale** — de Locale · es Idioma y región · fr Paramètres régionaux · hu Nyelvi beállítások · it Lingua e area geografica · ja ロケール · nl Taal en regio · pl Ustawienia regionalne · pt_BR Idioma · ro Setări regionale · ru Локаль · tr Yerel ayar · zh_CN 区域设置
- **Keyboard** — de Tastatur · es Teclado · fr Clavier · hu Billentyűzet · it Tastiera · ja キーボード · nl Toetsenbord · pl Klawiatura · pt_BR Teclado · ro Tastatură · ru Клавиатура · tr Klavye · zh_CN 键盘


## Add a desktop (X11)

ATT: **Desktop** → pick the desktop in the dropdown → **Install desktop**. Log out and
choose the new session on the SDDM login screen. Plasma and GNOME are one-way
installs (removing them needs a reinstall), and ATT warns before installing
them. After installing Plasma, see the Plasma fix in [faq.md](./faq.md).
See [desktops.md](./desktops.md) for the list.

Button labels in every ATT language (from ATT's own translations):

- **Desktop** — de Desktop · es Escritorio · fr Environnement de bureau · hu Asztali környezet · it Desktop · ja デスクトップ · nl Desktop · pl Środowisko · pt_BR Desktop · ro Desktop · ru Рабочий стол · tr Masaüstü · zh_CN 桌面
- **Install desktop** — de Desktop installieren · es Instalar escritorio · fr Installer l’environnement de bureau · hu Asztali környezet telepítése · it Installa desktop · ja デスクトップをインストール · nl Desktop installeren · pl Zainstaluj środowisko · pt_BR Instalar desktop · ro Instalează desktopul · ru Установить рабочий стол · tr Masaüstünü yükle · zh_CN 安装桌面


## Add a Wayland desktop

ATT: **Desktop - Wayland** → tick one or more → **Install selected**. If the
install button is grey, nemesis_repo was switched off: enable it (see below). Editions with
different shells (DMS, Noctalia, Noctura) can't be installed together. Log out
and pick the session at login. See [wayland.md](./wayland.md).

Button labels in every ATT language (from ATT's own translations):

- **Desktop - Wayland** — de Desktop - Wayland · es Escritorio - Wayland · fr Bureau : Wayland · hu Asztali környezet - Wayland · it Desktop - Wayland · ja デスクトップ - Wayland · nl Desktop - Wayland · pl Środowisko - Wayland · pt_BR Área de trabalho - Wayland · ro Desktop - Wayland · ru Рабочий стол - Wayland · tr Masaüstü - Wayland · zh_CN 桌面：Wayland
- **Install selected** — de Ausgewählte installieren · es Instalar seleccionados · fr Installer la sélection · hu Kijelöltek telepítése · it Installa selezionati · ja 選択したものをインストール · nl Geselecteerde installeren · pl Zainstaluj wybrane · pt_BR Instalar selecionados · ro Instalează selecția · ru Установить выбранные · tr Seçilenleri yükle · zh_CN 安装所选


## Install or switch kernels

ATT: **Kernels** → **Install {p}** next to a kernel ({p} is the kernel name);
**Set as Default** makes it the boot default. Keep two kernels installed.

Terminal: `sudo pacman -S linux-zen linux-zen-headers` (any kernel + its
headers). See [kernels.md](./kernels.md).

Button labels in every ATT language (from ATT's own translations):

- **Kernels** — de Kernels · es Kernels · fr Noyaux · hu Kernelek · it Kernel · ja カーネル · nl Kernels · pl Jądra · pt_BR Kernels · ro Kerneli · ru Ядра · tr Çekirdekler · zh_CN 内核
- **Install {p}** — de {p} installieren · es Instalar {p} · fr Installer {p} · hu {p} telepítése · it Installa {p} · ja {p} をインストール · nl {p} installeren · pl Zainstaluj {p} · pt_BR Instalar {p} · ro Instalează {p} · ru Установить {p} · tr {p} yükle · zh_CN 安装 {p}
- **Set as Default** — de Als Standard festlegen · es Establecer como predeterminada · fr Définir par défaut · hu Beállítás alapértelmezettként · it Imposta come predefinita · ja デフォルトに設定 · nl Als standaard instellen · pl Ustaw jako domyślny · pt_BR Definir como padrão · ro Setează ca implicit · ru Сделать по умолчанию · tr Varsayılan Yap · zh_CN 设为默认


## NVIDIA driver after installing with the open-drivers entry

Terminal (no reinstall needed):
```
kiro-hwd detect
sudo kiro-hwd install
```
Reboot. For a laptop with two GPUs, ATT **Hybrid graphics** → **Install missing
packages** sets up render offload (`prime-run`). See
[troubleshooting.md](./troubleshooting.md).

Button labels in every ATT language (from ATT's own translations):

- **Hybrid graphics** — de Hybridgrafik · es Gráficos híbridos · fr Graphisme hybride · hu Hibrid grafika · it Grafica ibrida · ja ハイブリッドグラフィックス · nl Hybride graphics · pl Grafika hybrydowa · pt_BR Gráficos híbridos · ro Grafică hibridă · ru Гибридная графика · tr Hibrit grafikler · zh_CN 混合显卡
- **Install missing packages** — de Fehlende Pakete installieren · es Instalar los paquetes que faltan · fr Installer les paquets manquants · hu Hiányzó csomagok telepítése · it Installa i pacchetti mancanti · ja 不足しているパッケージをインストール · nl Ontbrekende pakketten installeren · pl Zainstaluj brakujące pakiety · pt_BR Instalar pacotes que faltam · ro Instalează pachetele lipsă · ru Установить недостающие пакеты · tr Eksik paketleri yükleyin · zh_CN 安装缺少的软件包


## Snapshots before updates

- **btrfs install**: ATT **Btrfs** → **Enable snapshots** installs and configures
  snapper, snap-pac (a snapshot pair on every pacman action) and Btrfs
  Assistant to browse and restore. The page is grey on other file systems.
- **Any file system**: **Timeshift** ships on Kiro; open it from the menu and set
  up a schedule or take a snapshot before big changes.

Button labels in every ATT language (from ATT's own translations):

- **Btrfs** — de Btrfs · es Btrfs · fr Btrfs · hu Btrfs · it Btrfs · ja Btrfs · nl Btrfs · pl Btrfs · pt_BR Btrfs · ro Btrfs · ru Btrfs · tr Btrfs · zh_CN Btrfs
- **Enable snapshots** — de Snapshots aktivieren · es Activar instantáneas · fr Activer les instantanés · hu Pillanatképek engedélyezése · it Abilita snapshot · ja スナップショットを有効にする · nl Snapshots inschakelen · pl Włącz migawki · pt_BR Ativar snapshots · ro Activează instantaneele · ru Включить снимки · tr Anlık görüntüleri etkinleştir · zh_CN 启用快照


## Fix pacman keys and mirrors

ATT: **Maintenance** → Keys & GPG tab → **Fix keys**; Mirrors tab →
**Run rate-mirrors**.

Terminal: `kiro-fix-pacman-keys`, `kiro-fix-mirrors`, and if pacman.conf is
broken `kiro-fix-pacman-conf`. See [tools.md](./tools.md).

Button labels in every ATT language (from ATT's own translations):

- **Maintenance** — de Wartung · es Mantenimiento · fr Maintenance · hu Karbantartás · it Manutenzione · ja メンテナンス · nl Onderhoud · pl Konserwacja · pt_BR Manutenção · ro Întreținere · ru Обслуживание · tr Bakım · zh_CN 维护
- **Fix keys** — de Schlüssel reparieren · es Reparar claves · fr Réparer les clés · hu Kulcsok javítása · it Correggi le chiavi · ja キーを修正 · nl Sleutels herstellen · pl Napraw klucze · pt_BR Corrigir chaves · ro Repară cheile · ru Исправить ключи · tr Anahtarları düzelt · zh_CN 修复密钥
- **Run rate-mirrors** — de rate-mirrors ausführen · es Ejecutar rate-mirrors · fr Exécuter rate-mirrors · hu A rate-mirrors futtatása · it Esegui rate-mirrors · ja rate-mirrors を実行 · nl rate-mirrors uitvoeren · pl Uruchom rate-mirrors · pt_BR Executar o rate-mirrors · ro Rulează rate-mirrors · ru Запустить rate-mirrors · tr rate-mirrors çalıştır · zh_CN 运行 rate-mirrors


## Enable nemesis_repo (or chaotic-aur / cachyos)

On a fresh Kiro install nemesis_repo is already on. If it was removed, or on
another Arch system: ATT **Pacman** → **Enable Nemesis repo** (switches for
chaotic-aur and CachyOS sit next to it). Manual route: [faq.md](./faq.md),
"Can I use the nemesis_repo on a non-Kiro Arch system?".

Button labels in every ATT language (from ATT's own translations):

- **Pacman** — de Pacman · es Pacman · fr Pacman · hu Pacman · it Pacman · ja Pacman · nl Pacman · pl Pacman · pt_BR Pacman · ro Pacman · ru Pacman · tr Pacman · zh_CN Pacman
- **Enable Nemesis repo** — de Nemesis-Repo aktivieren · es Activar el repositorio Nemesis · fr Activer le dépôt Nemesis · hu A Nemesis tároló engedélyezése · it Abilita il repository Nemesis · ja Nemesis リポジトリを有効にする · nl Nemesis-repo inschakelen · pl Włącz repozytorium Nemesis · pt_BR Ativar o repositório Nemesis · ro Activează depozitul Nemesis · ru Включить репозиторий Nemesis · tr Nemesis deposunu etkinleştir · zh_CN 启用 Nemesis 软件源


## Change the default shell

Kiro's default shell is fish. ATT: **Shells** → the tab of the shell → **Apply
fish** / **Apply zsh** / **Apply bash**, then log out and in.

Terminal: `chsh -s /bin/zsh`, then log out and in.

Button labels in every ATT language (from ATT's own translations):

- **Shells** — de Shells · es Shells · fr Shells · hu Parancsértelmezők · it Shell · ja シェル · nl Shells · pl Powłoki · pt_BR Shells · ro Shell-uri · ru Оболочки · tr Kabuklar · zh_CN Shell
- **Apply fish** — de fish anwenden · es Aplicar fish · fr Appliquer fish · hu A fish alkalmazása · it Applica fish · ja fish を適用 · nl Fish toepassen · pl Zastosuj fish · pt_BR Aplicar fish · ro Aplică fish · ru Применить fish · tr Fish'i uygula · zh_CN 应用 fish
- **Apply zsh** — de zsh anwenden · es Aplicar zsh · fr Appliquer zsh · hu A zsh alkalmazása · it Applica zsh · ja zsh を適用 · nl Zsh toepassen · pl Zastosuj zsh · pt_BR Aplicar zsh · ro Aplică zsh · ru Применить zsh · tr Zsh'yi uygula · zh_CN 应用 zsh
- **Apply bash** — de bash anwenden · es Aplicar bash · fr Appliquer bash · hu A bash alkalmazása · it Applica bash · ja bash を適用 · nl Bash toepassen · pl Zastosuj bash · pt_BR Aplicar bash · ro Aplică bash · ru Применить bash · tr Bash'i uygula · zh_CN 应用 bash


## Firewall on or off

firewalld is on by default. ATT: **Network** → **Firewall** tab →
**Disable firewall** / **Enable firewall**. The same tab can allow network
discovery (mDNS) and Samba sharing, and installs the firewall-config GUI.

Terminal: `sudo systemctl disable --now firewalld` (or `enable --now`).

Button labels in every ATT language (from ATT's own translations):

- **Network** — de Netzwerk · es Red · fr Réseau · hu Hálózat · it Rete · ja ネットワーク · nl Netwerk · pl Sieć · pt_BR Rede · ro Rețea · ru Сеть · tr Ağ · zh_CN 网络
- **Firewall** — de Firewall · es Cortafuegos · fr Pare-feu · hu Tűzfal · it Firewall · ja ファイアウォール · nl Firewall · pl Zapora · pt_BR Firewall · ro Firewall · ru Брандмауэр · tr Güvenlik duvarı · zh_CN 防火墙
- **Disable firewall** — de Firewall deaktivieren · es Desactivar el cortafuegos · fr Désactiver le pare-feu · hu Tűzfal letiltása · it Disabilita il firewall · ja ファイアウォールを無効にする · nl Firewall uitschakelen · pl Wyłącz zaporę · pt_BR Desativar o firewall · ro Dezactivează firewall-ul · ru Отключить брандмауэр · tr Güvenlik duvarını devre dışı bırak · zh_CN 禁用防火墙
- **Enable firewall** — de Firewall aktivieren · es Activar el cortafuegos · fr Activer le pare-feu · hu Tűzfal engedélyezése · it Abilita il firewall · ja ファイアウォールを有効にする · nl Firewall inschakelen · pl Włącz zaporę · pt_BR Ativar o firewall · ro Activează firewall-ul · ru Включить брандмауэр · tr Güvenlik duvarını etkinleştir · zh_CN 启用防火墙


## Enable SSH

SSH is off by default. Terminal: `kiro-enable-ssh` installs openssh, enables
sshd and opens SSH in the firewall.

## Reset a desktop config to the Kiro defaults

Terminal: `kiro-skell` copies `/etc/skel` into the home folder and backs up the
`~/.config` entries it overwrites (`kiro-skell-all` backs up all of `~/.config`
first). Log out and in. Updates only change `/etc/skel`, so this is also how a
user gets new defaults on an existing account.

## Switch to a light theme

Change `GTK_THEME=Arc-Dawn-Dark` to `GTK_THEME=Arc` in `/etc/environment`
(`sudoedit /etc/environment`), then log out and in. Pick a matching icon theme
in ATT afterwards.

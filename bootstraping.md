### Вход в систему без пароля

### Переименовать VG
- Переименуем Volume Group

&nbsp;&nbsp;&nbsp;&nbsp;`# vgrename VolGroup00 OtusRoot`

- Редактируем /etc/fstab, /boot/grub2/grub.cfg и /etc/default/grub (прописываем новое имя группы)

- Пересоздаем initrd image, чтобы он знал новое название VG

&nbsp;&nbsp;&nbsp;&nbsp;`# mkinitrd -f -v /boot/initramfs-$(uname -r).img $(uname  -r)`

- Проверяем имя группы

&nbsp;&nbsp;&nbsp;&nbsp;`# vgs`

### Вход в систему без пароля
- способы описаны в методички Практика к уроку и успешно опробованы

### Переименовать VG
- Переименуем Volume Group

&nbsp;&nbsp;&nbsp;&nbsp;`# vgrename VolGroup00 OtusRoot`

- Редактируем /etc/fstab, /boot/grub2/grub.cfg и /etc/default/grub (прописываем новое имя группы)

- Пересоздаем initrd image, чтобы он знал новое название VG

&nbsp;&nbsp;&nbsp;&nbsp;`# mkinitrd -f -v /boot/initramfs-$(uname -r).img $(uname  -r)`

- Проверяем имя группы

&nbsp;&nbsp;&nbsp;&nbsp;`# vgs`

### Добавить кастомный модуль в initrd
- Создаем директорию в `/usr/lib/dracut/modules.d/` и помещаем туда скрипты из методички

&nbsp;&nbsp;&nbsp;&nbsp;  `# mkdir /usr/lib/dracut/modules.d/01test`

- Пересобираем образ initrd

&nbsp;&nbsp;&nbsp;&nbsp; `# dracut -f -v`

- Проверяем, какие модули загружены в образ

&nbsp;&nbsp;&nbsp;&nbsp; `# lsinitrd -m /boot/initramfs-$(uname -r).img | grep test`

- Перезагрузить и руками выключить опции rghb и quiet и увидеть ввод

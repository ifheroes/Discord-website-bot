# Discord-website-bot
Dieser Bot erlaubt die Synchronisation zwischen der Webseite von ifheroes.de und unserem Discord-Server

## Was soll der Bot können?

> 1. Der Bot soll Nachrichten aus dem Kanal 734524626490622033 in unserem Discord Kopieren 
> 2. In ein JSON-File mit Text, Link und Bild-Link ablegen
> 3. Der bot soll dies in regelmäßigen abständen überprüfen ob etwas neues gepostet wurde.

### Weitere Infos

> 1. In einer Datei, namens `config.json`, welche sich im Stammverzeichnis befindet, werden der Token, die Channel ID von dem Channel der geprüft werden soll und ein Präfix gespeichert. Ohne diese Datei wird der Bot nicht funktionieren. Hier ist der Inhalt der Datei:
>```json
>{
>    "token": "Bot Token",
>    "channel_id": "Channel ID",
>    "prefix": "Prefix"
>}
>```

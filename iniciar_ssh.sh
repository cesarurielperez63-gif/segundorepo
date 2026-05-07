#!/bin/bash
echo "inicializando agente SSH ..."
eval "$(ssh-agent -s)"
echo "agregando la clave SSH..."
ssh-add ~/.ssh/id_ed25519
echo "proceso Terminado."


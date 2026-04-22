Vscodeが保存できない場合
権限変更が必要になる

sudo chown -R $(whoami):$(whoami) .
chmod -R u+rwX .
で変更可能

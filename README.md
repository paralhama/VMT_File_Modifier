# VMT File Modifier 🔧📁
### O Que é Este Projeto?
Uma ferramenta para modificar arquivos .VMT (Valve Material Type) em projetos de modding, permitindo substituição de strings em múltiplos arquivos simultaneamente.

🎯 Propósito Específico

Substitui strings em arquivos .VMT de forma rápida e precisa, percorrendo TODAS as pastas e subpastas do diretório selecionado.

📝 Exemplo Prático
Você precisa alterar o caminho de varias texturas em vários arquivos .VMT onde será necessario altrar ```skins``` para ```skins_v2```
Antes da Modificação:
```
VertexLitGeneric
{
	"$basetexture" "skins\players\arthur_morgan\noarms"
	"$bumpmap"     "skins\players\arthur_morgan\noarms_nm"
}
```

Depois da Modificação:

```
VertexLitGeneric
{
	"$basetexture" "skins_v2\players\arthur_morgan\noarms"
	"$bumpmap"     "skins_v2\players\arthur_morgan\noarms_nm"
}
```

🔍 Como Funciona?
- Selecione o diretório raiz
- Insira a string original, exemplo: ```skins```
- Insira a nova string, exemplo: ```skins_v2```
- O script substituirá em:
   - Todos os arquivos .VMT
   - Em todas as pastas
   - Em todas as subpastas
   - Sem limites de profundidade

💡 Casos de Uso Comuns
- Atualização de caminhos de texturas
- Migração de versões de skins
- Reorganização de assets de jogos

🛡️ Segurança
- Não modifica arquivos sem a string exata
- Evita substituições duplicadas
- Mantém log detalhado das modificações


🚀 Como Usar
1. Execute o script ou o arquivo executável
2. Escolha o diretório raiz
3. Digite a string de busca
4. Digite a string de substituição
5. Clique em "Processar Arquivos VMT"

⚠️ Importante
- Sempre faça backup antes de usar
- Teste primeiro em uma cópia dos arquivos

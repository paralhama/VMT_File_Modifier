# VMT File Modifier 🔧📁
### O Que é Este Projeto?
Uma ferramenta para modificar arquivos .VMT (Valve Material Type) em projetos de modding, permitindo substituição de strings em múltiplos arquivos simultaneamente.

🎯 Propósito Específico

Substitui strings em arquivos .VMT de forma rápida e precisa, percorrendo TODAS as pastas e subpastas do diretório selecionado.

📝 Exemplo Prático

Antes da Modificação:
```
VertexLitGeneric
{
	"$basetexture" "fof_skins\players\arthur_morgan\noarms"
	"$bumpmap"     "fof_skins\players\arthur_morgan\noarms_nm"
}
```

Depois da Modificação:

```
VertexLitGeneric
{
	"$basetexture" "fof_skins_v2\players\arthur_morgan\noarms"
	"$bumpmap"     "fof_skins_v2\players\arthur_morgan\noarms_nm"
}
```

🔍 Como Funciona?
- Selecione o diretório raiz
- Insira a string original, exemplo: ```fof_skins```
- Insira a nova string, exemplo: ```fof_skins_v2```
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
3. Digite fof_skins como string de busca
4. Digite fof_skins_v2 como string de substituição
5. Clique em "Processar Arquivos VMT"

⚠️ Importante
- Sempre faça backup antes de usar
- Teste primeiro em uma cópia dos arquivos

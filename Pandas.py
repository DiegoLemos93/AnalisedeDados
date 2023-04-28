import pandas as pd

funcionario_df = pd.read_csv('CadastroFuncionarios.csv', sep=";", decimal=",")
clientes_df = pd.read_csv('CadastroClientes.csv', sep=";")
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

funcionario_df = funcionario_df.drop(['Estado Civil', 'Cargo'], axis=1) #axis=0 linha, axis=1 coluna

display(funcionario_df)
display(clientes_df)
display(servicos_df)

# Valor total da folha salarial:

funcionario_df['Salario Total'] = funcionario_df['Salario Base'] + funcionario_df['Impostos'] + funcionario_df['Beneficios'] + funcionario_df['VT'] + funcionario_df['VR']
print('O valor total da folha salarial mensal é de R${:,}.'.format(funcionario_df['Salario Total'].sum()))

# Faturamento total da empresa

faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['Valor Contrato Mensal', 'ID Cliente']], on='ID Cliente')
faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']
print('Faturamento total: R${:,}.'.format(faturamentos_df['Faturamento Total'].sum()))

# Percentual de funcionarios que fecharam contrato

qtde_funcionarios_fecharam_serviço = len(servicos_df['ID Funcionário'].unique())
qtde_funcionarios_total = len(funcionario_df['ID Funcionário'])
print('{:.2%} dos funcionarios fecharam contrato.'.format(qtde_funcionarios_fecharam_serviço / qtde_funcionarios_total))

# Qtde de contratos por area

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionario_df[['ID Funcionário', 'Area']], on='ID Funcionário')
contratos_area_qtde = contratos_area_df['Area'].value_counts()
print(contratos_area_qtde)
contratos_area_qtde.plot(kind='bar')

# Funcionarios por area

funcionarios_area = funcionario_df['Area'].value_counts()
print(funcionarios_area)
funcionarios_area.plot(kind='bar')

# Ticket médio mensal

ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('Ticket Medio Mensal: R${:,.2f}.'.format(ticket_medio))
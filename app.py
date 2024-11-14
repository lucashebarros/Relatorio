import streamlit as st
import pandas as pd

# Configurações da página
st.set_page_config(page_title="Proposta de Redução de Custos Power BI", layout="centered")

# Título
st.title("Proposta da empresa A2M Digital")

# Introdução
st.header("Introdução")
st.write("""
O portal A2M oferece uma solução White Label, **utilizando o Power BI Embedded**, que permite otimizar a gestão de relatórios e reduzir os custos com licenciamento.
""")

# Funcionamento na prática
st.header("Funcionamento na Prática")
st.write("""
O portal possui três níveis de usuários:
- **User Master**: Visualiza a empresa e gerencia filiais e departamentos.
- **User ADM**: Distribui relatórios aos departamentos e usuários.
- **User Visualizador**: Acessa relatórios específicos com opção de favoritos.
""")

# Vantagens
st.header("Vantagens do Portal A2M")
st.write("""
1. **Organização e Gestão**: Gestão centralizada e controlada dos relatórios.
2. **Experiência do Usuário**: Interface intuitiva e simplificada.
3. **Redução de Custos**: Menor necessidade de licenças PRO/PREMIUM, economizando mensalmente.
""")

# Proposta de Custo
st.header("Proposta de Custo")
st.write("""
- **Custo de Implantação**: R$ 700,00, parcelado em até 3x
- **Valor por Assinatura**: R$ 26,00 por usuário (para 5 usuários).
""")

# Tabela de Comparação de Economia de Custo
st.header("Comparação de Custos: Situação Atual vs Portal A2M")

# Dados para a tabela
data = {
    "Descrição": ["Licenciamento Atual (Power BI Pro)", "Licenciamento Futuro (a partir de Abril)", "Portal A2M + Power BI Embedded"],
    "Quantidade de Licenças": [5, 5, 5],
    "Custo por Licença": ["R$ 59,50", "R$ 81,30", "R$ 26,00"],
    "Custo Mensal Total": ["R$ 297,50", "R$ 406,50", "R$ 130,00"],
    "Custo Anual Total": ["R$ 3.570,00", "R$ 4.878,00", "R$ 1.560,00"],
    "Taxa de Implantação": ["-", "-", "R$ 700,00"]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Exibição da tabela
st.table(df)

# Cálculo das economias
st.write("""
**Economias Potenciais:**

- **Economia Mensal Atual**: 297,50 - 130,00" = **R$ 167,50**
- **Economia Anual Atual**: 3.570,00 - 1.560,00" = **R$ 2.010,00**

- **Economia Mensal Futura (a partir de Abril)**: 406,50 - 130,00" = **R$ 276,50**
- **Economia Anual Futura**: 4.878,00 - 1.560,00" = **R$ 3.318,00**
""")

# Recursos adicionais
st.header("Recursos e Features")
st.write("""
- **Hierarquia por setor e filial**: Controle e distribuição dos dashboards.
- **Central de Notificações**: Alertas para manutenções e atualizações.
- **Controle de Acesso**: Restrições de acesso por IP e horários.
- **Playlists para TVs**: Apresentação automatizada de relatórios.
- **Suporte Vitalício**: Suporte contínuo aos key users.
""")

# Teste gratuito e implementação
st.header("Teste e Implementação")
st.write("""
- **Teste PoC gratuito**: 7 dias de uso sem custo.
- **Custo de Implementação**: R$ 700,00 (único).
""")

# Conclusão
st.header("Conclusão")
st.write("""
A proposta da A2M representa uma oportunidade de otimizar a gestão de relatórios e reduzir os custos do Power BI, fornecendo um portal eficiente e integrado que simplifica o controle e acesso.

Com a iminente elevação dos custos das licenças do Power BI Pro a partir de Abril, a adoção do Portal A2M torna-se ainda mais vantajosa, proporcionando economias significativas e melhor gerenciamento dos recursos de BI.
""")

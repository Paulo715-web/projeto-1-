import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página para um visual moderno e escuro
st.set_page_config(
    page_title="Central IA - Assistente de Estudos", 
    page_icon="🤖", 
    layout="wide"
)

# Estilização CSS personalizada para visual de IA estilo ChatGPT/Gemini
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
    }
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #161B22;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (CONFIGURAÇÕES DO MODELO DE IA) ---
with st.sidebar:
    st.title("🤖 Configurações da IA")
    modelo_selecionado = st.selectbox(
        "Modelo de IA ativo:",
        ["Gemini 1.5 Flash (Rápido)", "Gemini 1.5 Pro (Avançado)", "EstudanteGPT (Modo Explicativo)"]
    )
    st.slider("Criatividade (Temperatura)", 0.0, 1.0, 0.7)
    st.divider()
    st.success(f"Status: **Conectado** via {modelo_selecionado}")
    st.caption("Central de Inteligência Artificial v2.0")

# --- CABEÇALHO DA APLICAÇÃO ---
st.title("⚡ Central Inteligente para Estudantes")
st.write("Sua plataforma interativa movida a Inteligência Artificial.")

# --- NAVEGAÇÃO POR ABAS ---
tab1, tab2, tab3 = st.tabs([
    "💬 Chat IA de Estudos", 
    "🧮 Assistente de Cálculos", 
    "🔍 Analisador de Documentos"
])

# --- ABA 1: CHAT DE IA INTERATIVO ---
with tab1:
    st.subheader("Conversa com a IA do Estudante")
    st.caption("Pergunte qualquer dúvida de matéria, peça resumos ou dicas de estudo!")

    # Histórico de conversa na sessão
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [
            {"role": "assistant", "content": "Olá! Sou o seu assistente de estudos com IA. Em que matéria posso ajudar hoje?"}
        ]

    # Exibe o histórico de mensagens
    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Entrada de texto para o utilizador enviar mensagem
    if prompt := st.chat_input("Digite sua dúvida (ex: 'Resuma a 2ª Lei de Newton')..."):
        # Guarda e mostra a mensagem do utilizador
        st.session_state.mensagens.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Resposta simulada da IA com efeito visual
        with st.chat_message("assistant"):
            with st.spinner("A pensar..."):
                resposta = f"🤖 **[Análise da IA]**: Excelente pergunta sobre '{prompt}'. Como assistente de estudos, aqui está uma explicação rápida:\n\n• **Ponto Principal:** O conceito chave envolve entender a lógica básica da matéria.\n• **Dica de Estudo:** Tente resolver um exercício prático para fixar melhor!"
                st.write(resposta)
                st.session_state.mensagens.append({"role": "assistant", "content": resposta})

# --- ABA 2: CALCULADORA E GRÁFICOS ---
with tab2:
    st.subheader("Cálculos Inteligentes e Gráficos")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        val_a = st.number_input("Valor A", value=3.0, step=1.0)
        val_b = st.number_input("Valor B", value=3.0, step=1.0)
        operacao = st.selectbox("Operação", ["Multiplicação (×)", "Adição (+)", "Subtração (-)", "Divisão (÷)"])
        
        if st.button("Executar Cálculo", type="primary"):
            if "Multiplicação" in operacao:
                res = val_a * val_b
            elif "Adição" in operacao:
                res = val_a + val_b
            elif "Subtração" in operacao:
                res = val_a - val_b
            else:
                res = val_a / val_b if val_b != 0 else 0
                
            st.session_state["resultado_calc"] = res

    with col2:
        if "resultado_calc" in st.session_state:
            res = st.session_state["resultado_calc"]
            st.success(f"### Resultado: **{res}**")
            
            # Gráfico dinâmico
            chart_data = pd.DataFrame({
                'Etapa': ['Valor A', 'Valor B', 'Resultado'],
                'Valores': [val_a, val_b, res]
            })
            st.bar_chart(chart_data.set_index('Etapa'))

# --- ABA 3: ANALISADOR DE IMAGENS/NOTAS ---
with tab3:
    st.subheader("Visão Computacional & Análise de Documentos")
    uploaded_file = st.file_uploader("Carregue uma imagem ou foto dos seus apontamentos:", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        col_img, col_txt = st.columns(2)
        with col_img:
            st.image(uploaded_file, caption="Ficheiro Carregado", use_container_width=True)
        with col_txt:
            st.info("🧠 **Análise Automática da IA:**")
            st.write("1. **Texto identificado:** Exemplo de Apontamentos.")
            st.write("2. **Qualidade da leitura:** 98% de precisão.")
            st.write("3. **Resumo gerado:** Conteúdo limpo e pronto para revisão.")
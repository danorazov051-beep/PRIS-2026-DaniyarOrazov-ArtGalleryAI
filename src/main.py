import streamlit as st
from mock_data import artwork
from logic import check_rules

st.title("Rule-Based Art Gallery System 🖼")

st.write("### Настройка параметров произведения")

price = st.sidebar.number_input(
    "Цена произведения",
    value=artwork["price"]
)

is_authentic = st.sidebar.checkbox(
    "Подлинное произведение",
    value=artwork["is_authentic"]
)

if st.button("Проверить произведение"):
    test_artwork = {
        "style": artwork["style"],
        "price": price,
        "tags": artwork["tags"],
        "is_authentic": is_authentic
    }

    result = check_rules(test_artwork)

    if "✅" in result:
        st.success(result)
    elif "⛔" in result:
        st.error(result)
    else:
        st.warning(result)

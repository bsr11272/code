mkdir -p ~/.streamlit/


echo "\
[theme]
base = "light"
" > ~/.streamlit/config.toml


echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

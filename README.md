# OpenAI GPT Model Serving API

Serve Openai GPT models locally for integration with frontend development
<p float="left">
     <img wdith=200 alt="figure 1" src="https://github.com/biomchen/openai-gpt-serving-api/assets/45435029/d1f87928-9063-4ba0-a777-e85b8e53dba5">
    <img width=200 alt="figure 2" src="https://github.com/biomchen/openai-gpt-serving-api/assets/45435029/dfa94baa-ee55-4c8a-98ca-2b8fe93cd4bf">
</p>


### Deployment
1. Create your own config file in JSON format using the `configs_sample.json` file
2. Set up your python env
    ```sh
    python3 -m venv YOUR_ENV_NAME
    ```
3. Activate the env in Mac OS and Ubuntu
    ```sh
    source YOUR_ENV_NAME/bin/activate
    ```
4. `pip` install required libraries
    ```sh
    pip isntall -r requirements.txt
    ```
x. Run the cmd in the terminal
    ```sh
    uvicorn serve:app --host 0.0.0.0 --port YOUR_DESIGNATED_PORT
    ```

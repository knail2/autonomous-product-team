import autogen

# import OpenAI API key
#config_list = autogen.config_list_from_json(env_or_file="code/OAI_CONFIG_LIST")
orca2_config_list_lmstudio = [{
        "base_url": "http://127.0.0.1:3010/v1",
        "api_key": "NULL"
}]
orca2_llm_config_lmstudio={"config_list": orca2_config_list_lmstudio}



# create the assistant agent
assistant = autogen.AssistantAgent(
    name="assistant", llm_config={"config_list": orca2_llm_config_lmstudio}
)

# Create the user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="UserProxy", code_execution_config={"work_dir": "results"}
)

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="Write a code to print odd numbers from 2 to 100."
)
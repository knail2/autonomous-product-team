import autogen
from githubfunctions import get_spiderman_code, send_pull_request

custom_function_list = [
    {
        "name" : "get_spiderman_code",
        "description" : "returns the python code for the spider man game in a string format"

    },
    {
        "name": "send_pull_request",
        "description" : "get the updated contents of the python code as a string, along with a suitable description for the commit and sends a pull request to the repo",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "new_content" : {
                    "type" : "string",
                    "description" : "the updated python code based on the changes requested in the prompt",
                },
                "branch_name" : {
                    "type" : "string",
                    "description" : "a suitable name of a code branch with no spaces",
                },
                "commit_description" : {
                    "type" : "string",
                    "description" : "a suitable commit description based on the changes made to the python code",
                },
            },
            "required": ["new_content", "branch_name", "commit_description"]
        },
    }
]

gpt_config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json"
    )

phi2_models = [{
        "base_url": "http://127.0.0.1:3010/v1",
        "api_key": "NULL"
}]
phi2_llm_config_lmstudio={"config_list": phi2_models}

# create an AssistantAgent named "assistant"
assistant = autogen.AssistantAgent(
    name="assistant",
    description="you are a python software coder",
    llm_config={
        "cache_seed": 43,  # seed for caching and reproducibility
        #"config_list": phi2_config_list_lmstudio,
        "config_list": gpt_config_list,  
        "temperature": 0,  # temperature for sampling
        "functions" : custom_function_list
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=3,
    #is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    },
    function_map={ "get_spiderman_code" : get_spiderman_code,
                  "send_pull_request" : send_pull_request
                  }
)

# the assistant receives a message from the user_proxy, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""get the spiderman code and modify the class to add some more interesting methods. 
    Then send a pull request with this code, using a unique and simple branch name, 
    along with a meaningful commit description""",
)
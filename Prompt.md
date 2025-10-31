Please use langchain and DeepSeek to create an agent:

- When the user asks `What is my IP?`, call function calling: `my_ip`
- The `my_ip` function will call the `https://httpbin.org/ip` REST API to get the user's IP address
- When the user asks `What's the weather like today?`, call function calling: `get_weather`
- The `get_weather` function will call the `https://api.weatherapi.com/v1/current.json` REST API to get current weather information
- For other questions, use the DeepSeek model to answer



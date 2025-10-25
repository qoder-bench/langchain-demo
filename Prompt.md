请使用langchain和DeepSeek创建一个智能体：

- 当用户询问`我的IP是多少?`时，调用function calling: `my_ip`
- `my_ip`函数会调用调用 `https://httpbin.org/ip` REST API 来获取用户的IP地址
- 当用户询问`今天的天气如何?`时，调用function calling: `get_weather`
- `get_weather`函数会调用 `https://api.weatherapi.com/v1/current.json` REST API 来获取当前天气信息
- 对于其他问题，使用DeepSeek模型进行回答
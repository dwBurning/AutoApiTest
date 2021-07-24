package response

type Response struct {
	Code    int         `json:"code"`
	Data    interface{} `json:"data"`
	Message string      `json:"message"`
}

func New(code int, msg string, data interface{}) Response {
	return Response{Code: code, Data: data, Message: msg}
}

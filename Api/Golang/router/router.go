package router

import (
	"api/controller"
	"github.com/gin-gonic/gin"
)

func InitRouter() *gin.Engine {

	r := gin.New()

	api := r.Group("/api")
	api.GET("/person", controller.Get)
	api.GET("/person/:id", controller.GetById)
	api.POST("/person", controller.Add)
	api.PATCH("person/:id",controller.Patch)
	api.DELETE("person/:id",controller.Delete)
	return r
}

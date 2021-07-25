package controller

import (
	"api/model"
	"api/response"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

var persons = make(map[int]model.Person)

func Get(ctx *gin.Context) {
	var ps []model.Person
	for _, v := range persons {
		ps = append(ps, v)
	}
	ctx.JSON(http.StatusOK, response.New(0, "获取成功", ps))
}

func GetById(ctx *gin.Context) {
	id := ctx.Param("id")
	key, _ := strconv.Atoi(id)
	person, ok := persons[key]

	if ok {
		ctx.JSON(http.StatusOK, response.New(0, "获取成功", person))
	} else {
		ctx.JSON(http.StatusOK, response.New(-1, "人事资料不存在", nil))
	}
}

func Delete(ctx *gin.Context) {
	id := ctx.Param("id")
	key, _ := strconv.Atoi(id)
	person, ok := persons[key]
	if ok {
		delete(persons, key)
		ctx.JSON(http.StatusOK, response.New(0, "删除成功", person))
	} else {
		ctx.JSON(http.StatusOK, response.New(-1, "人事资料不存在", nil))
	}
}

func Patch(ctx *gin.Context) {
	id := ctx.Param("id")
	key, _ := strconv.Atoi(id)
	person, ok := persons[key]

	if ok {
		var p model.Person
		ctx.ShouldBindJSON(&person)
		persons[key] = p
		ctx.JSON(http.StatusOK, response.New(0, "修改成功", nil))

	} else {
		ctx.JSON(http.StatusOK, response.New(-1, "人事资料不存在", nil))
	}

}

func Add(ctx *gin.Context) {
	var p model.Person
	ctx.ShouldBindJSON(&p)
	_, ok := persons[p.Id]
	if ok {
		ctx.JSON(http.StatusOK, response.New(-1, "人事资料已存在", nil))
	} else {
		persons[p.Id] = p
		ctx.JSON(http.StatusOK, response.New(0, "添加成功", nil))
	}

}

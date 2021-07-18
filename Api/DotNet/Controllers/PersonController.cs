using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AutoApiTest.Controllers
{
    /// <summary>
    /// 人事信息管理
    /// </summary>
    [ApiController]
    [Route("api/[controller]")]
    public class PersonController : ControllerBase
    {
        static List<Person> peoples = new List<Person>();

        /// <summary>
        /// 获取所有的人事信息
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        public OutPut<List<Person>> Get()
        {
            return new OutPut<List<Person>>() { Code = 0, Message = "获取成功", Data = peoples }; ;
        }

        /// <summary>
        /// 根据ID获取人事信息
        /// </summary>
        /// <returns></returns>
        [HttpGet("{id}")]
        public OutPut<Person> Get(int id)
        {
            var p = peoples.Find(x => x.Id == id);
            if (p != null)
            {
                return new OutPut<Person>() { Code = 0, Message = "获取成功", Data = p };
            }
            else
            {
                return new OutPut<Person>() { Code = -1, Message = "人事资料不存在" };
            }
        }

        /// <summary>
        /// 根据ID删除人事信息
        /// </summary>
        /// <param name="id"></param>
        [HttpDelete("{id}")]
        public OutPut<string> Delete(int id)
        {
            if (peoples.Remove(peoples.Find(x => x.Id == id)))
            {
                return new OutPut<string>() { Code = 0, Message = "删除成功" };
            }

            return new OutPut<string>() { Code = -1, Message = "人事资料不存在" };
        }

        /// <summary>
        /// 修改人事信息
        /// </summary>
        /// <param name="person"></param>
        /// <returns></returns>
        [HttpPatch("{id}")]
        public OutPut<string> Patch(Person person)
        {
            var p = peoples.Find(x => x.Id == person.Id);
            if (p != null)
            {
                p.Name = person.Name;
                p.Age = person.Age;
                return new OutPut<string>() { Code = 0, Message = "修改成功" };
            }
            else
            {
                return new OutPut<string>() { Code = -1, Message = "人事资料不存在" };
            }
        }

        /// <summary>
        /// 新增人事资料
        /// </summary>
        /// <param name="person"></param>
        /// <returns></returns>
        [HttpPost]
        public OutPut<string> Post(Person person)
        {
            var p = peoples.Find(x => x.Id == person.Id);
            if (p != null)
            {
                return new OutPut<string>() { Code = -1, Message = "人事资料已存在" };
            }
            else
            {
                peoples.Add(person);
                return new OutPut<string>() { Code = 0, Message = "添加成功" };
            }
        }


    }
}

using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace AutoApiTest
{
    /// <summary>
    /// 人事信息
    /// </summary>
    public class Person
    {
        /// <summary>
        /// ID
        /// </summary>
        [Required]
        public int Id { get; set; }

        /// <summary>
        /// 名字
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        /// 年龄
        /// </summary>
        public int Age { get; set; }
    }
}

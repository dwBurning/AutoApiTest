using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AutoApiTest
{
    public class OutPut<T> where T : class
    {
        public int Code { get; set; }

        public string Message { get; set; }

        public T Data { get; set; }
    }
}

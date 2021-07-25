package auto.test.api.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import auto.test.api.models.OutPut;
import auto.test.api.models.Person;

@RestController
@RequestMapping(value = "api/person")
public class PersonController {

	static List<Person> persons;

	public PersonController() {
		persons = new ArrayList<Person>();
	}

	@RequestMapping(method = RequestMethod.GET)
	public OutPut<List<Person>> get() {
		OutPut<List<Person>> outPut = new OutPut<List<Person>>();
		outPut.setCode(0);
		outPut.setData(persons);
		outPut.setMessage("获取成功");
		return outPut;
	}

	@RequestMapping(value = "/{id}", method = RequestMethod.GET)
	public OutPut<Person> Get(@PathVariable("id") int id) {
		Person person = persons.stream().filter(x -> x.getId() == id).findFirst().orElse(null);
		if (person != null) {
			OutPut<Person> outPut = new OutPut<Person>();
			outPut.setCode(0);
			outPut.setData(person);
			outPut.setMessage("获取成功");
			return outPut;
		} else {
			OutPut<Person> outPut = new OutPut<Person>();
			outPut.setCode(-1);
			outPut.setData(person);
			outPut.setMessage("人事资料不存在");
			return outPut;
		}
	}

	@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
	public OutPut<String> delete(@PathVariable("id") int id) {
		Person person = persons.stream().filter(x -> x.getId() == id).findFirst().orElse(null);
		if (persons.remove(person)) {
			OutPut<String> outPut = new OutPut<String>();
			outPut.setCode(0);
			outPut.setMessage("删除成功");
			return outPut;
		} else {
			OutPut<String> outPut = new OutPut<String>();
			outPut.setCode(-1);
			outPut.setMessage("人事资料不存在");
			return outPut;
		}
	}

	@RequestMapping(method = RequestMethod.PATCH)
	public OutPut<String> Patch(@RequestBody Person person) {
		Person p = persons.stream().filter(x -> x.getId() == person.getId()).findFirst().orElse(null);
		if (p != null) {
			p.setName(person.getName());
			p.setAge(person.getAge());
			OutPut<String> outPut = new OutPut<String>();
			outPut.setCode(0);
			outPut.setMessage("修改成功");
			return outPut;
		} else {
			OutPut<String> outPut = new OutPut<String>();
			outPut.setCode(-1);
			outPut.setMessage("人事资料不存在");
			return outPut;
		}
	}

	@RequestMapping(method = RequestMethod.POST)
	public OutPut<String> post(@RequestBody Person person) {
		Person p = persons.stream().filter(x -> x.getId() == person.getId()).findFirst().orElse(null);
		if (p != null) {
			OutPut<String> outPut = new OutPut<String>();
			outPut.setCode(-1);
			outPut.setMessage("人事资料已存在");
			return outPut;
		} else {
			persons.add(person);
			OutPut<String> outPut = new OutPut<String>();
			outPut.setCode(0);
			outPut.setMessage("添加成功");
			return outPut;

		}
	}
}

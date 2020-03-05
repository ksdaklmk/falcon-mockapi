from locust import HttpLocust, TaskSet, task, between


class TestDiis(TaskSet):

    def on_start(self):
        self.client.post("/login", {
            "username": "test",
            "password": ""
        })

    def on_stop(self):
        pass

    @task
    def sign_request(self):
        self.client.get("http://localhost:5000")


class PerfTest(HttpLocust):

    task_set = TestDiis
    wait_time = between(5, 15)
    
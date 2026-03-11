from locust import HttpUser, task, between


class GUDLFTUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.email = "kate@shelifts.co.uk"
        self.client.post("/showSummary", data={"email": self.email})

    @task(3)
    def load_homepage(self):
        with self.client.get("/", catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure("Homepage too slow (>5s)")

    @task(2)
    def load_clubs_dashboard(self):
        with self.client.get("/clubs", catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure("Clubs dashboard too slow (>5s)")

    @task(2)
    def show_summary(self):
        with self.client.post(
            "/showSummary",
            data={"email": self.email},
            catch_response=True
        ) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure("ShowSummary too slow (>5s)")

    @task(1)
    def purchase_places(self):
        with self.client.post(
            "/purchasePlaces",
            data={
                "club": "She Lifts",
                "competition": "Spring Festival",
                "places": "1",
            },
            catch_response=True
        ) as response:
            if response.elapsed.total_seconds() > 2:
                response.failure("PurchasePlaces too slow (>2s)")

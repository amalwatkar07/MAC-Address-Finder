from flask import Flask, render_template
from network_info import get_network_info

app = Flask(__name__)


@app.route("/")
def home():
    network_data = get_network_info()

    total_interfaces = len(network_data)

    active_interfaces = sum(
        1 for network in network_data
        if network["status"] == "Active"
    )

    inactive_interfaces = total_interfaces - active_interfaces

    return render_template(
        "index.html",
        networks=network_data,
        total=total_interfaces,
        active=active_interfaces,
        inactive=inactive_interfaces
    )


if __name__ == "__main__":
    app.run(debug=True)
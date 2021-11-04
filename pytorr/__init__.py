import qbittorrentapi
from flask import Flask
from flask import jsonify
from flask import render_template

# instantiate a Client using the appropriate WebUI configuration
qbt_client = qbittorrentapi.Client(
    host="https://qbittorrent.seluj78.fr", port=443, username="seluj78", password="J2fg@51dgxW-"
)
application = Flask(__name__)


@application.route("/")
def home():
    return render_template("qbit_stats.html")


@application.route("/qbit_stats")
def qbit_stats():
    all_stats = qbt_client.sync.maindata()["server_state"]
    alltime_dl = all_stats["alltime_dl"]
    alltime_ul = all_stats["alltime_ul"]
    connection_status = all_stats["connection_status"]
    free_space_on_disk = all_stats["free_space_on_disk"]
    global_ratio = all_stats["global_ratio"]
    total_peer_connections = all_stats["total_peer_connections"]
    dl_info_data = all_stats["dl_info_data"]
    dl_info_speed = all_stats["dl_info_speed"]
    up_info_data = all_stats["up_info_data"]
    up_info_speed = all_stats["up_info_speed"]

    returned_stats = {
        "alltime_dl": alltime_dl,
        "alltime_ul": alltime_ul,
        "connection_status": connection_status,
        "free_space_on_disk": free_space_on_disk,
        "global_ratio": global_ratio,
        "total_peer_connections": total_peer_connections,
        "dl_info_data": dl_info_data,
        "dl_info_speed": dl_info_speed,
        "up_info_data": up_info_data,
        "up_info_speed": up_info_speed,
    }

    return jsonify(returned_stats)

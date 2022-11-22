from sklearn.cluster import DBSCAN


def db_cluster(data):
    db = DBSCAN(eps=0.05, min_samples=2).fit(data)
    dl = db.labels_
    c_min, c_max = 0, 0
    for l in dl:
        c_min = min(c_min, l)
        c_max = max(c_max, l)
    return dl, c_max - c_min + 1

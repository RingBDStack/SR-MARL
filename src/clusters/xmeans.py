from sklearn.cluster import KMeans
import numpy as np
import math


def kmeans(data, k, index=None):
    """
    :param data: (n_samples, n_features)
    :param k: cluster number
    :return: 聚类结果及集群失真
    """
    model = KMeans(n_clusters=k, random_state=0)
    model.fit(data)
    labels = model.labels_
    centers = model.cluster_centers_
    distortion = model.inertia_
    clusters = list()
    for i in range(k):
        clusters.append(dict())
        clusters[i]['data'] = []
        clusters[i]['index'] = []
        clusters[i]['cluster_centers'] = centers[i]
    for i in range(len(labels)):
        clusters[labels[i]]['data'].append(data[i])
        if index == None:
            clusters[labels[i]]['index'].append(i)
        else:
            clusters[labels[i]]['index'].append(index[i])
    result = dict()
    result['clusters'] = clusters
    result['distortion'] = distortion
    return result


def old_bic(n, d, distortion):
    """
    :param n: n_samples
    :param d: n_features
    :param distortion: 集群失真
    :return: BIC分数
    """
    variance = distortion / (n - 1)
    p1 = -n * math.log(math.pi * 2)
    p2 = -n * d * math.log(variance)
    p3 = - (n - 1)
    L = (p1 + p2 + p3) / 2
    numParameters = d + 1
    return L - 0.5 * numParameters * math.log(n)


def loglikelihood(k, n, ni, d, variance):
    """
    :param k: cluster number
    :param n: n_samples
    :param ni: 此类样本数
    :param d: n_features
    :param variance: 集群的估计方差
    :return: 后验概率估计值
    """
    p1 = -ni * math.log(math.pi * 2)
    p2 = -ni * d * math.log(variance)
    p3 = -(ni - k)
    p4 = ni * math.log(ni)
    p5 = -ni * math.log(n)
    loglike = (p1 + p2 + p3) / 2 + p4 + p5
    return loglike


def new_bic(k, n, d, distortion, clustersSize):
    """
    :param k: cluster number
    :param n: n_samples
    :param d: n_features
    :param distortion: 集群失真
    :param clustersSize: 各聚类样本数量，(k, 1)
    :return: BIC分数
    """
    variance = distortion / (n - k)
    L = 0.0
    for i in range(k):
        L += loglikelihood(k, n, clustersSize[i], d, variance)
    numParameters = k + k * d
    return L - 0.5 * numParameters * math.log(n)


def Xmeans(data, kmin, kmax):
    """
    :param data: (n_samples, n_features)
    :return: 聚类结果及集群失真
    """
    d = data.shape[0]
    k = kmin
    init_clusters = kmeans(data, k)
    while k < kmax:
        wscc = np.zeros((k, 1))
        for i in range(k):
            center = init_clusters['clusters'][i]['cluster_centers']
            for tmp_sample in init_clusters['clusters'][i]['data']:
                wscc += np.sqrt(np.sum(np.square(np.array(tmp_sample) - np.array(center))))
        split2cluster = dict()
        for i in range(k):
            if len(init_clusters['clusters'][i]['data']) <= 2:
                continue
            my2means = kmeans(init_clusters['clusters'][i]['data'], 2, init_clusters['clusters'][i]['index'])
            old_bic_score = old_bic(len(init_clusters['clusters'][i]['data']), d, wscc[i])
            new_bic_score = new_bic(2, len(init_clusters['clusters'][i]['data']), d, my2means['distortion'],
                                    [len(my2means['clusters'][0]['data']), len(my2means['clusters'][1]['data'])])
            if new_bic_score > old_bic_score:
                split2cluster[i] = my2means
        for key in split2cluster.keys():
            init_clusters['clusters'][key] = split2cluster[key]['clusters'][0]
            init_clusters['clusters'].append(dict())
            init_clusters['clusters'][k] = split2cluster[key]['clusters'][1]
            k += 1
        if split2cluster == {}:
            break
    results = [0] * data.shape[0]
    for i in range(len(init_clusters['clusters'])):
        for j in init_clusters['clusters'][i]['index']:
            results[j] = i
    return results, len(init_clusters['clusters'])

get_ip = function () {
    var a, i, json, l, _i, _len;
    l = [];
    a = document.getElementsByTagName("tr");
    for (_i = 0, _len = a.length; _i < _len; _i++) {
        i = a[_i];
        json = {
            "ip": i.innerText.split("\t")[1],
            "title": i.innerText.split("\t")[3],
            "mark": ""
        };
        l.push(json);
    }
    return l;
};

get_proxy_ip = function () {
    l = []
    a = document.getElementsByTagName('tr');
    for (var i = 0; i < a.length; i++) {
        json = {
            'ip': a[i].innerText.split('\t')[1],
            "title": a[i].innerText.split("\t")[3],
            "mark": ""
        };
        l.push(json);
    }
    return l
}
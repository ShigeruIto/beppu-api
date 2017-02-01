
function file_json(url)
{
        httpObj = new XMLHttpRequest();
        httpObj.open("get", url, false);
	httpObj.send(null);
        return JSON.parse(httpObj.responseText);
}

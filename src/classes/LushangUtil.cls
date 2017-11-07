/**************************************************************************************************
 * Name: LushangUtil
 * Object: 
 * Purpose: Utility Class
 * Author: Lushang
 * Create Date: 2016-11-05
 * Modified History: 
***************************************************************************************************/
public  class LushangUtil {

    public static String SendHttpPOSTwithXML(String endPoint, String body) {
        return sendHttpRequest(endPoint, 'POST', body , 'text/xml;charset=UTF-8');
    }

    public static String SendHttpPOSTwithJSON(String endPoint, String body) {
        return sendHttpRequest(endPoint, 'POST', body , 'application/json;charset=UTF-8');
    }

    public static String SendHttpGETwithXML(String endPoint) {
        return sendHttpRequest(endPoint, 'GET', null , 'text/xml;charset=UTF-8');
    }

    public static String SendHttpGETwithJSON(String endPoint) {
        return sendHttpRequest(endPoint, 'GET', null , 'application/json;charset=UTF-8');
    }

    public static Blob RequestBlob(String url, String method, String body) {
        HttpRequest req = new HttpRequest();
        req.setEndpoint(url);
        req.setMethod(method);
        if (body != null)
            req.setBody(body);
        Http http = new Http();
        HttpResponse res = http.send(req);
        return res.getBodyAsBlob();
    }

    public static String sendHttpRequest(String endPoint, String method, String body, Map<String, String> headerMap) {
        HttpRequest req = new HttpRequest();
        Http http = new Http();

        try {
            req.setMethod(method);
            for (String headKey : headerMap.keySet()) {
                req.setHeader(headKey, headerMap.get(headKey));
            }
            req.setEndpoint(endPoint);
            if (body != null) {
                req.setBody(body);
            }

            HttpResponse res = http.send(req);
            if (res.getStatus() == 'OK') {
                return res.getBody();
            } else {
                return 'Error';
            }
        } catch (Exception e) {
            System.debug(LoggingLevel.INFO, '*** e.getMessage(): ' + e.getMessage());
            return e.getMessage();
        }
    }

}
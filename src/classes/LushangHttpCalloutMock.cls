/**************************************************************************************************
 * Name: LushangHttpCalloutMock
 * Object: 
 * Purpose: Mock HTTP response for test class
 * Author: Lushang (tyler@lushang.me)
 * Create Date: 2016-11-15
 * Modify History:
 * 2016-11-15    Lushang    Create
 **************************************************************************************************/
@isTest
global class LushangHttpCalloutMock implements HttpCalloutMock {

    public static final String MOCKFSOENDPOINT = 'https://sample.com';

    // The map of end point => response body
    private static Map<String, String> bodyMap;
    private static Boolean testException = false;

    static {
        bodyMap = new Map<String, String>();
        bodyMap.put(LushangConfig.USER_LIST_ENDPOINT, 
            '{"total":2,"count":2,"data":{"openid":["","o6_bmjrPTlm6_2sgVt7hMZOPfL2M","OPENID2"]},"next_openid":"NEXT_OPENID"}');

    }


    // Generate the end point map when construct the class
    public WeChatHttpCalloutMock(Boolean isException) {
        testException = isException;
    }

    public WeChatHttpCalloutMock() {
        testException = false;
    }

    // Implement this interface method
    global HTTPResponse respond(HTTPRequest req) {

        String endPoint = req.getEndpoint();
        HttpResponse res;

        if (testException == false) {
            // For the normal test, with the right flow
            if (req.getMethod() == 'POST') {
                if (endPoint == MOCKFSOENDPOINT) {
                    res = generateResponse(GetaEIdResponseBody());
                
                } else if (endPoint.contains(LushangConfig.CUSTOM_MENU_CREATION_ENDPOINT)) {
                    res = GenerateResponse(bodyMap.get(LushangConfig.CUSTOM_MENU_CREATION_ENDPOINT));
                
                }

            } else if (req.getMethod() == 'GET') {
                if ( endPoint.contains(LushangConfig.USER_INFO_ENDPOINT) ||
                     endPoint.contains(LushangConfig.AUTH2_USER_INFO_ENDPOINT) ) {
                    res = GenerateResponse(bodyMap.get(LushangConfig.USER_INFO_ENDPOINT));
                
                } else if (endPoint.contains(LushangConfig.USER_LIST_ENDPOINT)) {
                    res = GenerateResponse(bodyMap.get(LushangConfig.USER_LIST_ENDPOINT));
                
                } else if (endPoint.contains(LushangConfig.ACCESS_TOKEN_ENDPOINT)) {
                    res = GenerateResponse(bodyMap.get(LushangConfig.ACCESS_TOKEN_ENDPOINT));
                
                } else if (endPoint.contains(LushangConfig.MATERIAL_COUNT_ENDPOINT)) {
                    res = GenerateResponse(bodyMap.get(LushangConfig.MATERIAL_COUNT_ENDPOINT));
                
                } else if (endPoint.contains(LushangConfig.GET_QR_URL)) {
                    res = GenerateImageResponse();
                
                } else if (endPoint.contains(LushangConfig.WEB_AUTH2_ENDPOINT)) {
                    res = GenerateResponse(bodyMap.get(LushangConfig.WEB_AUTH2_ENDPOINT));
                
                }

            } else if (req.getMethod() == 'DELETE') {
                res = generateResponse('success');

            } else {
                res = null;
            }
        // For the test of Exception
        } else {
            if (endPoint == MOCKFSOENDPOINT) {
                res = generateResponse(bodyMap.get('acceidException'));

            } else if (endPoint.contains(LushangConfig.ACCESS_TOKEN_ENDPOINT)) {
                    res = GenerateResponse('{"errcode":40013,"errmsg":"invalid appid"}');
                
                } 
        }
        System.debug(LoggingLevel.INFO, '*** resBody: ' + res.getBody());
        return res;
    }

    private HttpResponse GenerateResponse(String body) {

        // Create a fake response
        HttpResponse res = new HttpResponse();
        res.setHeader('Content-Type', 'application/json');
        res.setBody(body);
        res.setStatusCode(200);
        res.setStatus('OK');
        return res;
    }

    private HttpResponse GenerateImageResponse() {

        // Create a fake response
        HttpResponse res = new HttpResponse();
        res.setHeader('Content-Type', 'image/jpg');
        res.setBodyAsBlob(Blob.valueOf('String o'));
        res.setStatusCode(200);
        res.setStatus('OK');
        return res;
    }

    private HttpResponse GenerateBadResponse(Integer code, String body) {

        // Create a fake response
        HttpResponse res = new HttpResponse();
        res.setHeader('Content-Type', 'application/json');
        res.setBody(body);
        res.setStatusCode(code);
        return res;
    }

    private String GetaEIdResponseBody() {
        return '{"msg":"ok", "code":0, "data":{"key":"88886666' + Math.rint(Math.random()*1000) + '"}}';
    }
}
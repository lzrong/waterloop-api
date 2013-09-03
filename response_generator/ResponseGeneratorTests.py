from ResponseGenerator import ResponseGenerator

print("An example success payload:")
ResponseGenerator.generateSuccess("Test", {"test": "An embedded dictionary"}, "1234567890")

print("\n\nAn example failure payload:")
ResponseGenerator.generateFailure("Test", {"error": {"password": "An example error would have a tag like this"}}, "1234567890")

print("\n\nAn example failure payload, note the different error code options:")
ResponseGenerator.generateFailure("Test", {"error": {"token": "Your session has expired, please log back in"}}, "1234567890", errorCode = "403")

print("\n\nAn example exception payload:")
try:
    raise Exception("An exception has been raised - all scripts should execute in try-except blocks")
except Exception as e:
    ResponseGenerator.generateExceptionNotice(e, "1234567890")
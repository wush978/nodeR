#include <node.h>
#include <v8.h>
#include <RInside.h>

using namespace v8;

Handle<Value> HelloR(const Arguments& args) {
	  HandleScope scope;
	    return scope.Close(String::New("world"));
}

void init(Handle<Object> exports) {
	  exports->Set(String::NewSymbol("helloR"),
			        FunctionTemplate::New(HelloR)->GetFunction());
}

NODE_MODULE(helloR, init)

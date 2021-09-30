package hello;
import io.sentry.Sentry;


public class HelloWorld {

    public static void main(String[] args) {
        new Sentry.init(options -> {
          options.setDsn("https://a8423d7609d341679d54302626f296d9@o1019220.ingest.sentry.io/5986317");
          options.setTracesSampleRate(1.0);
          options.setDebug(true);
          });

        Greeter greeter = new Greeter();
        System.out.println(greeter.sayHello());
    }
}
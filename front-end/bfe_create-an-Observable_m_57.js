class Observable {
    setup = null;

    constructor(source) {
        this.source = source;
    }

    subscribe(destination) {
        const subscriber = new Subscriber(destination);
        return new Subscription(subscriber, this.source);
    }
}

class Subscription {
    isSubscribed = true;
    _subscriber = null;

    constructor(
        subscriber,
        source,
    ) {
        this._subscriber = subscriber;
        source(subscriber);
    }

    unsubscribe() {
        this._subscriber.isActive = false;
        this.isSubscribed = false;
    }
}

class Subscriber {
    isActive = true;
    destination = null;

    constructor(destination) {
        this.destination = typeof destination === "function"
            ? { next: destination }
            : destination;
    }

    next(val) {
        if (this.isActive && this.destination.next) {
            this.destination.next(val);
        }
    }

    error(val) {
        if (this.isActive && this.destination.error) {
            this.isActive = false;
            this.destination.error(val);
        }
    }

    complete() {
        if (this.isActive && this.destination.complete) {
            this.isActive = false;
            this.destination.complete();
        }
    }
}

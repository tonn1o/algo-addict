class Observable {
    subscribers = new Set();
    onSubscribe = null;

    constructor(setup) {
        this.onSubscribe = (newSubscriber) => setup({
            next: (val) => this._next(val, newSubscriber),
            error: (val) => this._error(val, newSubscriber),
            complete: () => this._complete(newSubscriber),
        });
    }

    subscribe(subscriber) {
        this.subscribers.add(subscriber);
        this.onSubscribe(subscriber);

        return {
            unsubscribe: this._createUnsubscribe(subscriber)
        };
    }

    _createUnsubscribe(subscriber) {
        return () => this.subscribers.delete(subscriber);
    }

    _next(val, subscriber) {
        if (!this.subscribers.has(subscriber)) {
            return;
        }

        if (subscriber.hasOwnProperty('next')) {
            subscriber.next(val);
        } else if (typeof subscriber === 'function') {
            subscriber(val);
        }
    }

    _error(val, subscriber) {
        if (!this.subscribers.has(subscriber)) {
            return;
        }

        if (subscriber.hasOwnProperty('error')) {
            subscriber.error(val);
        }

        this.subscribers.delete(subscriber);
    }

    _complete(subscriber) {
        if (!this.subscribers.has(subscriber)) {
            return;
        }

        if (subscriber.hasOwnProperty('complete')) {
            subscriber.complete();
        }

        this.subscribers.delete(subscriber);
    }
}


// TEST
const obs = new Observable((subscriber) => {
    subscriber.next(1);
    subscriber.next(2);
    subscriber.next(3);
    // subscriber.complete();

    setTimeout(() => subscriber.next(4), 1000)
});

const sub = obs.subscribe({
    next: val => {
        console.log(val)
    }
});

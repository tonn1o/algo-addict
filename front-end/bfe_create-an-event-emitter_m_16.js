class EventEmitter {
    _subscriptions = new Map()

    subscribe(event, cb) {
        const sub = new Subscription(event, cb);
        const eventSubs = this._subscriptions.get(event) || [];

        this._subscriptions.set(event, [...eventSubs, sub]);

        return new Subscribed(this._subscriptions, sub);
    }

    emit(event, ...data) {
        const eventSubscribers = this._subscriptions.get(event);

        if (eventSubscribers && eventSubscribers.length) {
            eventSubscribers.forEach((sub) => sub.cb(...data));
        }
    }
}

class Subscription {
    constructor(event, cb) {
        this.event = event;
        this.cb = cb;
    }
}

class Subscribed {
    constructor(subscriptions, sub) {
        this._subscirptions = subscriptions;
        this._sub = sub
    }

    release() {
        const eventSubs = this._subscirptions.get(this._sub.event);
        const subIdx = eventSubs.indexOf(this._sub);
        eventSubs.splice(subIdx, 1);
    }
}

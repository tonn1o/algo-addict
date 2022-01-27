class Emitter {
    events = new Map();

    subscribe(eventName, cb) {
        if (this.events.has(eventName)) {
            this.events.get(eventName).add(cb);
        } else {
            this.events.set(eventName, new Set([cb]));
        }

        return {
            release: () => {
                this.events.get(eventName).delete(cb);

                if (this.events.get(eventName).size === 0) {
                    this.events.delete(eventName);
                }
            }
        }
    }

    emit(eventName, ...args) {
        if (this.events.has(eventName)) {
            this.events.get(eventName).forEach(cb => cb(...args));
        }
    }
}

const emitter = new Emitter();

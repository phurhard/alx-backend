const kue = require('kue');

const queue = kue.createQueue();

const job_data = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

const push_notification_code = queue.create('push_notification_code', job_data);
push_notification_code.save(function(err) {
    if (err) {
        console.log('Notification job failed');
    } else {
        console.log('Notification job created: ', push_notification_code.id);
        push_notification_code.on('complete', ()=> {
            console.log('Notification job completed');
        });
        push_notification_code.on('failed', ()=> {
            console.log('Notification job failed');
        });
    }
});

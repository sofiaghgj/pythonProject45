def instance_to_user(instance):
    return {
        "id": instance.id,
        "first_name": instance.first_name,
        "last_name": instance.last_name,
        "age": instance.age,
        "email": instance.email,
        "role": instance.role,
        "phone": instance.phone,
    }


def instance_to_oder(instance):
    return {
        "id": instance.id,
        "name": instance.name,
        "description": instance.description,
        "start_date": instance.start_date,
        "end_date": instance.end_date,
        "address": instance.address,
        "price": instance.price,
        "customer_id": instance.customer_id,
        "executor_id": instance.executor_id,
    }


def instance_to_offer(instance):
    return {
        "id": instance.id,
        "order_id": instance.order_id,
        "executor_id": instance.executor_id,
    }

import click 
import file
from datetime import datetime

current_datetime = datetime.now()

@click.group()
def cli():
    pass 


@cli.command()
def users():
    data  = file.read_json()
    for user in data:
        print(f"""Id: {user['id']}  -  Title: {user['title']}  -  Description: {user['description']}  
            - Status: {user['status']} -  Create at: {user['createdAt']}  -  Update at: {user['updateAt']}""")


@cli.command()
@click.argument('id', type=int)
@click.option('--title', help="update the title")
@click.option('--description', help="update the description")
@click.option('--status', help="update the status")
def update(id,title,description,status):
    data = file.read_json()
    for t in data:
        if t['id'] == id:
            t['updateAt'] = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            if title is not None:
                t['title'] = title
            if description is not None:
                t['description'] = description
            if status is not None:
                t['status'] = status 
            break
    file.write_json(data)
    print(f"The Task with id {id} updated successfully")





@cli.command()
@click.option('--title', required=True, help= 'Name of the task')
@click.option('--description', required=True, help= 'Description of the task')
@click.option('--status', required=False, help= 'Description of the status the project')
@click.pass_context
def newTask(ctx, title, description,status):
    if not title or not description:
        ctx.fail('The title and description are required')
    else:
        data = file.read_json()
        new_id = len(data) + 1
        new_task = {
            'id': new_id,
            'title': title,
            'description': description,
            'status': status,
            'createdAt': current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'updateAt': 'No update',
        }
        data.append(new_task)
        file.write_json(data)
        print(f"Tarea {title} created successfully")

@cli.command()
@click.argument('id', type=int)
def getTask(id):
    data = file.read_json()
    t = next((x for x in data if x['id'] == id), None)
    if t is None:
            print(f"Task with id {id} not found")
    else:
        print(f"""
                Id: {t['id']} 
                Title: {t['title']}
                Description: {t['description']}
                Status: {t['status']}
                Created at: {t['createdAt']}
                Update at: {t['updateAt']}""")
    
@cli.command()
@click.argument('id', type=int)
def deleteTask(id):
    data = file.read_json()
    t = next((x for x in data if x['id'] == id), None)
    if t is None:
        print(f"The Task with title: {id} not found")
    else:
        data.remove(t)
        print(f"The task with id: {id} removed")
        file.write_json(data)
if __name__ == '__main__':
    cli()

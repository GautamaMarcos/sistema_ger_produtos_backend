# Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

# Garantir que o diretório static exista antes de aplicar as permissões
RUN mkdir -p /usr/src/app/static && chmod -R 755 /usr/src/app/static

# Garantir permissões corretas para o diretório static
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput
# Exponha a porta que seu aplicativo Django usará
EXPOSE 8000

# Comando para iniciar o aplicativo em produção usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sistema_ger_produtos.wsgi:application"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
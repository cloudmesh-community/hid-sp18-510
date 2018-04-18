SWAGGER_CODEGEN=java -jar $(SWAG_DIR)/swagger-codegen-cli.jar
YAML_FILE=aml.yaml
DEST_DIR=server
TEST_DIR=test
SWAG_DIR=swagger
TRAIN_DIR=$(DEST_DIR)/model
CONFIG_DIR=cloudmesh

dirs:
	mkdir -p $(TEST_DIR)
	mkdir -p $(DEST_DIR)
	mkdir -p $(CONFIG_DIR)
	
swagger:
	mkdir -p $(SWAG_DIR)
	cd $(SWAG_DIR) && wget http://central.maven.org/maven2/io/swagger/\
	swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar \
	-O swagger-codegen-cli.jar
	
docker-build:
	docker build -t nkaul/swagger .
	
docker-start:
	docker run -p 8080:8080 nkaul/swagger
	
docker-start-detach-mode:
	docker run -d -p 8080:8080 nkaul/swagger

docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

train:
	mkdir -p $(TRAIN_DIR)
	cp controller_train.py $(TRAIN_DIR)
	cd $(TRAIN_DIR) && python controller_train.py
	
service: dirs swagger
	#Install and Generate the service
	$(SWAGGER_CODEGEN) generate -i $(YAML_FILE) -l python-flask -o $(DEST_DIR) -D supportPython3=true
	cp -r default_controller.py $(DEST_DIR)/swagger_server/controllers
	#cp -r auth_util.py $(DESTDIR)/swagger_server/controllers
	#cp -r __main__.py $(DEST_DIR)/swagger_server/
	cp -r $(YAML_FILE) $(CONFIG_DIR)
	cd $(DEST_DIR) && pip install -r requirements.txt && \
	python setup.py install

start:
	#starts the services
	cd $(DEST_DIR) && python -m swagger_server

stop:
	#stops the service
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

test:
	#executes tests against the service
	cp test_client.py $(TEST_DIR)
	cd $(TEST_DIR); python test_client.py; cd ..;

clean: 
	# removes the code generated
	if [ -d $(DEST_DIR) ]; then rm -r $(DEST_DIR); fi
	if [ -d $(TEST_DIR) ]; then rm -rf $(TEST_DIR); fi
	if [ -d $(CONFIG_DIR) ]; then rm -r $(CONFIG_DIR); fi
	if [ -d $(SWAG_DIR) ]; then rm -r $(SWAG_DIR); fi
	if [ -d $(TRAIN_DIR) ]; then rm -r $(TRAIN_DIR); fi


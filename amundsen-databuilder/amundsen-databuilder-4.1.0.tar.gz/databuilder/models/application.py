# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import List, Union

from databuilder.models.graph_node import GraphNode
from databuilder.models.graph_relationship import GraphRelationship
from databuilder.models.graph_serializable import GraphSerializable
from databuilder.models.table_metadata import TableMetadata


class Application(GraphSerializable):
    """
    Application-table matching model (Airflow task and table)
    """

    APPLICATION_LABEL = 'Application'
    APPLICATION_KEY_FORMAT = 'application://{cluster}.airflow/{dag}/{task}'
    APPLICATION_URL_NAME = 'application_url'
    APPLICATION_NAME = 'name'
    APPLICATION_ID = 'id'
    APPLICATION_ID_FORMAT = '{dag_id}/{task_id}'
    APPLICATION_DESCRIPTION = 'description'
    APPLICATION_TYPE = 'Airflow'

    APPLICATION_TABLE_RELATION_TYPE = 'GENERATES'
    TABLE_APPLICATION_RELATION_TYPE = 'DERIVED_FROM'

    def __init__(self,
                 task_id: str,
                 dag_id: str,
                 application_url_template: str,
                 db_name: str = 'hive',
                 cluster: str = 'gold',
                 schema: str = '',
                 table_name: str = '',
                 exec_date: str = '',
                 ) -> None:
        self.task = task_id

        # todo: need to modify this hack
        self.application_url = application_url_template.format(dag_id=dag_id)
        self.database, self.cluster, self.schema, self.table = db_name, cluster, schema, table_name

        self.dag = dag_id

        self._node_iter = iter(self.create_nodes())
        self._relation_iter = iter(self.create_relation())

    def create_next_node(self) -> Union[GraphNode, None]:
        # creates new node
        try:
            return next(self._node_iter)
        except StopIteration:
            return None

    def create_next_relation(self) -> Union[GraphRelationship, None]:
        try:
            return next(self._relation_iter)
        except StopIteration:
            return None

    def get_table_model_key(self) -> str:
        # returns formatted string for table name
        return TableMetadata.TABLE_KEY_FORMAT.format(db=self.database,
                                                     schema=self.schema,
                                                     tbl=self.table,
                                                     cluster=self.cluster)

    def get_application_model_key(self) -> str:
        # returns formatting string for application of type dag
        return Application.APPLICATION_KEY_FORMAT.format(cluster=self.cluster,
                                                         dag=self.dag,
                                                         task=self.task)

    def create_nodes(self) -> List[GraphNode]:
        """
        Create a list of Neo4j node records
        :return:
        """
        results = []
        application_description = '{app_type} with id {id}'.format(
            app_type=Application.APPLICATION_TYPE,
            id=Application.APPLICATION_ID_FORMAT.format(dag_id=self.dag, task_id=self.task)
        )
        application_id = Application.APPLICATION_ID_FORMAT.format(
            dag_id=self.dag,
            task_id=self.task
        )
        application_node = GraphNode(
            key=self.get_application_model_key(),
            label=Application.APPLICATION_LABEL,
            attributes={
                Application.APPLICATION_URL_NAME: self.application_url,
                Application.APPLICATION_NAME: Application.APPLICATION_TYPE,
                Application.APPLICATION_DESCRIPTION: application_description,
                Application.APPLICATION_ID: application_id
            }
        )
        results.append(application_node)

        return results

    def create_relation(self) -> List[GraphRelationship]:
        """
        Create a list of relations between application and table nodes
        :return:
        """
        graph_relationship = GraphRelationship(
            start_key=self.get_table_model_key(),
            start_label=TableMetadata.TABLE_NODE_LABEL,
            end_key=self.get_application_model_key(),
            end_label=Application.APPLICATION_LABEL,
            type=Application.TABLE_APPLICATION_RELATION_TYPE,
            reverse_type=Application.APPLICATION_TABLE_RELATION_TYPE,
            attributes={}
        )
        results = [graph_relationship]
        return results

# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import functools
from asynctestcase import AsyncDocumentTranslationTest
from preparer import DocumentTranslationPreparer, DocumentTranslationClientPreparer as _DocumentTranslationClientPreparer
from azure.ai.documenttranslation import DocumentTranslationInput, TranslationTarget
from azure.ai.documenttranslation.aio import DocumentTranslationClient
import pytest
DocumentTranslationClientPreparer = functools.partial(_DocumentTranslationClientPreparer, DocumentTranslationClient)


class TestAllDocumentStatuses(AsyncDocumentTranslationTest):

    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    async def test_list_statuses(self, client):
        # prepare containers and test data
        blob_data = [b'This is some text']
        source_container_sas_url = self.create_source_container(data=blob_data)
        target_container_sas_url = self.create_target_container()
        target_language = "es"

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[
                    TranslationTarget(
                        target_url=target_container_sas_url,
                        language_code=target_language
                    )
                ]
            )
        ]

        # submit and validate job
        job_id = await self._submit_and_validate_translation_job_async(client, translation_inputs, len(blob_data))

        # check doc statuses
        doc_statuses = client.list_all_document_statuses(job_id)
        doc_statuses_list = []

        async for document in doc_statuses:
            doc_statuses_list.append(document)
            self._validate_doc_status(document, target_language)

        self.assertEqual(len(doc_statuses_list), len(blob_data))



    @pytest.mark.skip("top not exposed yet")
    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    async def test_list_statuses_with_pagination(self, client):
        # prepare containers and test data
        blob_data = [b'text 1', b'text 2', b'text 3', b'text 4', b'text 5', b'text 6']
        source_container_sas_url = self.create_source_container(data=blob_data)
        target_container_sas_url = self.create_target_container()
        result_per_page = 2
        no_of_pages = len(blob_data) // result_per_page
        target_language = "es"

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[
                    TranslationTarget(
                        target_url=target_container_sas_url,
                        language_code=target_language
                    )
                ]
            )
        ]

        # submit and validate job
        job_id = await self._submit_and_validate_translation_job_async(client, translation_inputs, len(blob_data))

        # check doc statuses
        doc_statuses_pages = client.list_all_document_statuses(job_id=job_id, results_per_page=result_per_page)
        pages_list = []

        # iterate by page
        async for page in doc_statuses_pages:
            pages_list.append(page)
            page_docs_list = []
            async for document in page:
                page_docs_list.append(document)
                self._validate_doc_status(document, target_language)
            self.assertEqual(len(page_docs_list), result_per_page)

        self.assertEqual(len(pages_list), no_of_pages)



    @pytest.mark.skip("skip not exposed yet")
    @DocumentTranslationPreparer()
    @DocumentTranslationClientPreparer()
    async def test_list_statuses_with_skip(self, client):
        # prepare containers and test data
        blob_data = [b'text 1', b'text 2', b'text 3', b'text 4', b'text 5', b'text 6']
        source_container_sas_url = self.create_source_container(data=blob_data)
        target_container_sas_url = self.create_target_container()
        docs_len = len(blob_data)
        skip = 2
        target_language = "es"

        # prepare translation inputs
        translation_inputs = [
            DocumentTranslationInput(
                source_url=source_container_sas_url,
                targets=[
                    TranslationTarget(
                        target_url=target_container_sas_url,
                        language_code=target_language
                    )
                ]
            )
        ]

        # submit and validate job
        job_id = await self._submit_and_validate_translation_job_async(client, translation_inputs, len(blob_data))

        # check doc statuses
        doc_statuses = client.list_all_document_statuses(job_id=job_id, skip=skip)
        doc_statuses_list = []

        # iterate over docs
        async for document in doc_statuses:
            doc_statuses_list.append(document)
            self._validate_doc_status(document, target_language)

        self.assertEqual(len(doc_statuses_list), docs_len - skip)
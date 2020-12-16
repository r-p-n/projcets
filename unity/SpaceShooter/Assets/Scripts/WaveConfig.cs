using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WaveConfig : MonoBehaviour
{
    [SerializeField]
    private GameObject enemyPrefab;
    [SerializeField]
    private int enemyFleet = 10;
    [SerializeField]
    private float spawnRate = 2f;
    [SerializeField]
    private int delay;

    void Start()
    {
        Invoke("StartSpawner", delay);
    }

    void StartSpawner()
    {
        StartCoroutine("Spawn");
    }

    IEnumerator Spawn()
    {
        for (int i=0; i<enemyFleet; i++)
        {
            Instantiate(enemyPrefab, transform.position, Quaternion.identity);

            yield return new WaitForSeconds(spawnRate);
        }
    }
}
